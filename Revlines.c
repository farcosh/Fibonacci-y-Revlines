#include <stdio.h>
#include <wctype.h>
#include <string.h>
#define SIZE 10000

//Metodo quenos ayuda a limpiar las cadenas que genera fgets
//ya que de no hacerlo al imprimirlo, tendriamos una invalidacion 
//en la memoria
void limpiar (char *cadena){
  char *p;
  p = strchr (cadena, '\n');
  if (p)
    *p = '\0';
}

//Metodo que imprime el archivo en orden inverso, usando la pila
//de ejecucion y fgets
void imprimir(FILE * fp){
	char str[SIZE];
	if(feof(fp)){
		return;
	}else{
		fgets(str, sizeof(str), fp);
		imprimir(fp);
		limpiar(str);
		printf("%s\n", str);
	}
}


int main (int argc, const char * argsv[]){
	FILE * fp;
	//Captura de error; Si el programa no recibe argumentos
	if(argc <= 1){
		printf("Error\n");
		return -1;
	}
	//Abrimos el archivo que se nos dio en modo "lectura" = "r"
	fp = fopen(argsv[1], "r");
    //Captura de error por si algo sale mal con la lectura
	if(fp == NULL){
		printf("Archivo vacio");
		return -1;
	}
	imprimir(fp);
	return 1;
}
