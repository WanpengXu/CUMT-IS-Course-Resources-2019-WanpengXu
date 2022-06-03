 int main(){
    int BX=0x100;
    do{
        int CX=0xFFFF;
        do{
            int DX=0x100;
	        do{
	            ;
	            DX--;
	        }
	        while(DX!=0);
            CX--;
        }
        while(CX!=0);
        BX--;
    }
    while(BX!=0);
    return 0;
}
