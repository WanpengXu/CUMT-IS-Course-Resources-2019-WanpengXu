#include "RC6.hpp"

RC6::RC6(unsigned int W, unsigned int R, unsigned int B){
  w = W;
  r = R;
  b = B;
  log_w = (unsigned int)log2(w);
  modulo = std::pow(2, w);
  S = new unsigned int[2 * r + 4];
}

void RC6::rc_constraints(const unsigned int &w, unsigned int &p, unsigned int &q){
  p = (unsigned int)std::ceil(((M_E - 2) * std::pow(2, w)));
  q = (unsigned int)((1.618033988749895 - 1) * std::pow(2, w));    // Golden Ratio
}

/******************************************************************
 * Function: left_rot
 * Input: <int> a, <unsigned int> b, <unsigned int> w
 * Output: int
 * Description: Rotate the w-bit word a to the left by the amount
 *              given by the least significant log w bits of b
 ******************************************************************/
int RC6::left_rot(unsigned int a, unsigned int b, unsigned int w){
  b <<= w - log_w;
  b >>= w - log_w;
  return (a << b) | (a >> (w - b));  
}

/******************************************************************
 * Function: right_rot
 * Input: <int> a, <unsigned int> b, <unsigned int> w
 * Output: int
 * Description: Rotate the w-bit word a to the right by the amount
 *              given by the least significant log w bits of b
 ******************************************************************/
int RC6::right_rot(unsigned int a, unsigned int b, unsigned int w){
  b <<= w - log_w;
  b >>= w - log_w;
  return (a >> b) | (a << (w - b));
}

/******************************************************************
 * Function: little_endian
 * Input: <std::string>
 * Output: std::string
 * Description: Convert input string to little endian version by bytes
 *              and return new little endian string. Assuming
 *              each character represents a byte
 ******************************************************************/
std::string RC6::little_endian(std::string str){
  std::string endian;
  
  if(str.length() % 2 == 0){
    for(std::string::reverse_iterator r_it = str.rbegin();
	     r_it != str.rend();r_it = r_it + 2){
      endian.push_back(*(r_it+1));
      endian.push_back(*r_it);
    }
  }else{
    str = "0" + str;
    for(std::string::reverse_iterator r_it = str.rbegin();
      r_it != str.rend();r_it = r_it + 2){
      endian.push_back(*(r_it+1));
      endian.push_back(*r_it);
    }
  }

  return endian;
}

std::string RC6::hex_to_string(unsigned int A, unsigned int B, unsigned int C, unsigned int D){

  std::string strA, strB, strC, strD, result;

  std::stringstream ss;
  ss << std::setfill('0') << std::setw(4) <<std::hex << A;
  strA = little_endian(ss.str());
  ss.str("");
  ss.clear();

  ss << std::setfill('0') << std::setw(4) <<std::hex << B;
  strB = little_endian(ss.str());
  ss.str("");
  ss.clear();
  
  ss << std::setfill('0') << std::setw(4) <<std::hex << C;
  strC = little_endian(ss.str());
  ss.str("");
  ss.clear();

  ss << std::setfill('0') << std::setw(4) <<std::hex << D;
  strD = little_endian(ss.str());
  ss.str("");
  ss.clear();

  result = strA + strB + strC + strD;

  return result;

}

/******************************************************************
 * Function: key_schedule
 * Input: <std::string> key
 * Output: void
 * Description: Generates the key schedule for RC6. 
 *              The input takes the user-supplied b byte key preloaded
 *              in c-word L[0, ... , c-1]
 *              The function then outputs the w-bit round keys
 *              S[0, ... , 2r+3]
 ******************************************************************/
void RC6::key_schedule(std::string key){
  const unsigned int w_bytes = std::ceil((float)w / 8);
  const unsigned int c = std::ceil((float)b / w_bytes);

  unsigned int p, q;
  rc_constraints(w, p, q);

  L = new unsigned int[c];
  for(int i = 0; i < c; i++){
    L[i] = strtoul(little_endian(key.substr(w_bytes * 2 * i, w_bytes * 2)).c_str(), NULL, 16);
  }  

  S[0] = p;
  for(int i = 1; i <= (2 * r + 3); i++){
    S[i] = (S[i - 1] + q) % modulo;
  }

  unsigned int A = 0, B = 0, i = 0, j = 0;
  int v = 3 * std::max(c, (2 * r + 4));
  for(int s = 1; s <= v; s++){
    A = S[i] = left_rot((S[i] + A + B) % modulo, 3, w);
    B = L[j] = left_rot((L[j] + A + B) % modulo, (A + B), w);
    i = (i + 1) % (2 * r + 4);
    j = (j + 1) % c;
  }
}

/******************************************************************
 * Function: encrypt
 * Input: <const std::string>
 * Output: std::string
 * Description: Encrypt plaintext from the input string to ciphertext
 ******************************************************************/
std::string RC6::encrypt(const std::string &text){
  std::string result;
  
  unsigned int A, B, C, D;
  A = strtoul(little_endian(text.substr(0, 8)).c_str(), NULL, 16);
  B = strtoul(little_endian(text.substr(8, 8)).c_str(), NULL, 16);
  C = strtoul(little_endian(text.substr(16, 8)).c_str(), NULL, 16);
  D = strtoul(little_endian(text.substr(24, 8)).c_str(), NULL, 16);

  int32_t t, u, temp;

  B += S[0];
  D += S[1];
  for(int i = 1; i <= r; ++i){
    t = left_rot((B * (2 * B + 1)) % modulo, log_w, w);
    u = left_rot((D * (2 * D + 1)) % modulo, log_w, w);
    A = left_rot((A ^ t), u , w) + S[2 * i];
    C = left_rot((C ^ u), t, w) + S[2 * i + 1];
    temp = A;
    A = B;
    B = C;
    C = D;
    D = temp;
  }

  A += S[2 * r + 2];
  C += S[2 * r + 3];

  result = hex_to_string(A, B, C, D);

  return result;
}

/******************************************************************
 * Function: decrypt
 * Input: <const std::string>
 * Output: std::string
 * Description: decrypt ciphertext from the input string to plaintext
 ******************************************************************/
std::string RC6::decrypt(const std::string &text){
  std::string result;
  
  unsigned int A, B, C, D;
  A = strtoul(little_endian(text.substr(0, 8)).c_str(), NULL, 16);
  B = strtoul(little_endian(text.substr(8, 8)).c_str(), NULL, 16);
  C = strtoul(little_endian(text.substr(16, 8)).c_str(), NULL, 16);
  D = strtoul(little_endian(text.substr(24, 8)).c_str(), NULL, 16);

  unsigned int t, u, temp;  
  
  C -= S[2 * r + 3];
  A -= S[2 * r + 2];
  for(int i = r; i >= 1; --i){
    temp = D;
    D = C;
    C = B;
    B = A;
    A = temp;
    u = left_rot((D * (2 * D + 1)) % modulo, log_w, w);
    t = left_rot((B * (2 * B + 1)) % modulo, log_w, w);
    C = right_rot((C - S[2 * i + 1]) % modulo, t, w) ^ u;
    A = right_rot((A - S[2 * i]) % modulo, u, w) ^ t;
  }
  D -= S[1];
  B -= S[0];

  result = hex_to_string(A, B, C, D);

  return result;
}



std::string RC6::run(const std::string &mode, const std::string &text, const std::string &key){

  std::string result;

  key_schedule(key);
  
  if(mode.compare(0, strlen("Encryption"), "Encryption") == 0){
    std::string encryption = encrypt(text);
    for(std::string::iterator it = encryption.begin(); it != encryption.end();it = it + 2){
      result.push_back(*it);
      result.push_back(*(it+1));
      result = result + " ";
    }
  }else if(mode.compare(0, strlen("Decryption"), "Decryption") == 0){
    std::string decryption = decrypt(text);
    for(std::string::iterator it = decryption.begin(); it != decryption.end();it = it + 2){
      result.push_back(*it);
      result.push_back(*(it+1));
      result = result + " ";
    }
  }

  return result;
}

RC6::~RC6(){
  delete S;
}
