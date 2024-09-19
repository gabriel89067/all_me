#include<stdio.h>
#include<math.h>
#include<string.h>
int main()
{
    int tat[100],q,w,e,tam,joga,joga2,c2,r,y,b,x,c,n,i,k,ganhou,perdeu,o,p,m,f,g,tyu,inicio,aubi,cv,bn;
    char min[100][100],vet[10000],vet1[10000];
  m=0;
  q=0;
  c=0;
  k=0;
scanf("%i",&inicio);
 aubi=0;
 while(aubi != inicio){

scanf("%i",&tam);

    for(i=0;i<tam;++i){
     for(n=0;n<tam;++n){

       scanf("%s",&min[i][n]);

    }}


    for(o=0;o<tam;++o){ //transformar matriz em m para saber quantos 'x' eu tenho
     for(p=0;p<tam;++p){
         min[o][p];
         if(min[o][p]== 'x')
         m++;
       
        }}





   scanf("%i",&joga);  //jogadas

         while(c<=joga){ //modifica os integrantes adgacentes para nao serem 'x'.
           scanf("%i %i",&x ,&y);//5 x  4 jogadas
            vet[c] = min[x][y];

              if(min[x][y]=='x'){
               min[x][y] = 'v';
                m--;
            }
            if(min[x-1][y-1] == 'b'){//caso o bloco selecionado seja de vizinhança com alguma bomba (bn) sera diferente de zero diminuindo somente o x do bloco selecionado
            bn++;}
            if(min[x-1][y] == 'b'){
            bn++;}
            if(min[x-1][y+1] == 'b'){
            bn++;}
            if(min[x][y-1] == 'b'){
            bn++;}
            if(min[x][y+1] == 'b'){
            bn++;}
            if(min[x+1][y-1] == 'b'){
            bn++;}
            if(min[x+1][y] == 'b'){
            bn++;}
            if(min[x+1][y+1] == 'b'){
            bn++;}


             if(bn==0){

            if(min[x-1][y-1] == 'x'){
              min[x-1][y-1] = 'v';
                m--;
            }
             if(min[x-1][y] == 'x'){
               min[x-1][y] = 'v';
                m--;
            }
            if(min[x-1][y+1] == 'x'){
            min[x-1][y+1] = 'v';
                m--;
            }
            if(min[x][y-1] == 'x'){
              min[x][y-1]  = 'v';
                m--;
            }
            if(min[x][y+1] == 'x'){
               min[x][y+1]  = 'v';
                m--;
            }
            if(min[x+1][y-1] == 'x'){
              min[x+1][y-1]  = 'v';
                m--;
            }
            if(min[x+1][y] == 'x'){
               min[x+1][y] = 'v';
                m--;
            }
            if(min[x+1][y+1] == 'x'){
              min[x+1][y+1] = 'v';
                m--;
            }}
            
            c++;
            bn=0;}

tyu = 0;

for(e=0;e<c;e++){   //verifica se existe algum 'b' selecionado.
            if(vet[e] == 'b'){
            tyu++;
            break;}

            }


if(tyu != 0){ //se existir algum 'b' entao (tyu != 0)=(por conta do (for) anteriro).
     printf("PERDEU\n");}


 if(tyu == 0){

    if(m != 0){// m e o numero de 'x' no tabuleiro, se (m != 0) faltou remover algum x. ******************************************

    printf("FALTOU TERMINAR\n");
    goto fim;

 }else{
printf("GANHOU\n");}//caso (m = 0) entao o numero de 'x' escolhidos/adjacentes foram selecionados.
   }

fim:
 m=0;
  q=0;
  c=0;
  k=0;
  tyu=0;
aubi++;}

return 0;
}
