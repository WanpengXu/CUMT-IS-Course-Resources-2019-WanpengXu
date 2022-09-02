#ifndef RC6_HPP__
#define RC6_HPP__

#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <iomanip>
#include <stdint.h>

class RC6{

private:

  // Declarations
  unsigned int w, r, b, log_w;    // w:     word size in bits 
                                  //        (default: 32 bits / 4 bytes)
                                  // r:     nonnegative number of rounds
                                  // b:     length of the encryption key in bytes
                                  // log_w: base-two logarithm of w
  int64_t modulo;        // modulo:2 ^ w
  std::string mode, text, key;    // mode:  encryption or decryption
                                  // text:  text to excrypt or decrypt
                                  // key:   user supplied key
  unsigned int *S;                // s:     stores the number of w-bits words
                                  //        that will be generated for the 
                                  //        additive round keys is 2r+4
  unsigned int *L;

  // RC6 Functons

  // Gets RC6 "magic constraints"
  void rc_constraints(const unsigned int &, unsigned int &, unsigned int &);

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
  void key_schedule(std::string key);

  /******************************************************************
   * Function: encrypt
   * Input: <const std::string>
   * Output: std::string
   * Description: Encrypt plaintext from the input string to ciphertext
   ******************************************************************/
  std::string encrypt(const std::string &);
  
  /******************************************************************
   * Function: decrypt
   * Input: <const std::string>
   * Output: std::string
   * Description: decrypt ciphertext from the input string to plaintext
   ******************************************************************/
  std::string decrypt(const std::string &);
 

  /******************************************************************
   * Function: left_rot
   * Input: <int> a, <unsigned int> b, <unsigned int> w
   * Output: int
   * Description: Rotate the w-bit word a to the left by the amount
   *              given by the least significant log w bits of b
   ******************************************************************/
  int left_rot(unsigned int, unsigned int, unsigned int);

  /******************************************************************
   * Function: right_rot
   * Input: <int> a, <unsigned int> b, <unsigned int> w
   * Output: int
   * Description: Rotate the w-bit word a to the right by the amount
   *              given by the least significant log w bits of b
   ******************************************************************/
  int right_rot(unsigned int, unsigned int, unsigned int);

  /******************************************************************
   * Function: little_endian
   * Input: <std::string>
   * Output: std::string
   * Description: Convert input string to little endian version by bytes
   *              and return new little endian string
   ******************************************************************/
  std::string little_endian(std::string);

  std::string hex_to_string(unsigned int A, unsigned int B, unsigned int C, unsigned int D);

public:
  // RC6-w/r/b
  RC6(unsigned int W = 32, unsigned int R = 20, unsigned int B = 16);

  //run RC6
  std::string run(const std::string &, const std::string &, const std::string &);

  ~RC6();
};

#endif
