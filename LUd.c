#include <stdio.h>
#include<math.h>
#include <gsl/gsl_permutation.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_linalg.h>
int main(){
double a[9]={1,.67,.33,.45,1,.55,.67,.33,1};
double L[3][3]={{1,0,0},{0,1,0},{0,0,1}};
double U[3][3]={{0,0,0},{0,0,0},{0,0,0}};
double LU[3][3]={{0,0,0},{0,0,0},{0,0,0}};
double ans[3][3]={{0,0,0},{0,0,0},{0,0,0}};

gsl_matrix * b=gsl_matrix_alloc(3,3);  //allocate 3x3 matrices
gsl_permutation * I=gsl_permutation_alloc(3); 


b->data=a;
printf("Given matrix\n");
for (int i = 0; i < 9; ++i)
{
	printf("%f ",a[i]);
	if ((i+1)%3==0)
	{
		printf("\n");
	}
}
int sig=0;
printf("\n");
int x=gsl_linalg_LU_decomp(b,I,&sig);

 //Convert vector to matrix
for (int i = 0; i < 9; ++i)
{
	ans[i/3][i%3]=b->data[i];
}                                      

printf("Matrix obtained after using gsl function\n");
for (int i = 0; i < 3; ++i)
{
	for (int j = 0; j < 3; ++j)
	{
		printf("%f",ans[i][j]);
	}
printf("\n");                         
}


 //extracting L and U matrices from ans
for (int i = 0; i < 3; ++i)
{
	for (int j = 0; j < 3; ++j)
	{
		if (i<=j)
		{
			U[i][j]=ans[i][j];
		}
		else{
			L[i][j]=ans[i][j];
		}
	}
}  

printf("Lower triangular matrix\n");
for (int i = 0; i < 3; ++i)
{
	for (int j = 0; j < 3; ++j)
	{
		printf("%f",L[i][j]);
	}
printf("\n");                         
}
printf("Upper triangular matrix\n");
for (int i = 0; i < 3; ++i)
{
	for (int j = 0; j < 3; ++j)
	{
		printf("%f",U[i][j]);
	}
printf("\n");                         
}                                      

//multiply L and U, check if the multiplication gives given matrix

for (int i = 0; i < 3; ++i)
{
	for (int j = 0; j < 3; ++j)
	{
		for (int k = 0; k < 3 ; ++k)
		{
			LU[i][j]+=L[i][k]*U[k][j];
		}
		
	}
}
printf("\n");
//print multiplication of L and U. In output compare 1st and 3rd matrices. They will(should) be same.
printf("multiplication of L and U matrices\n");
for (int i = 0; i < 3; ++i)
{
	for (int j = 0; j < 3; ++j)
	{
		printf("%f",LU[i][j]);
	}
printf("\n");                         
}


gsl_matrix_free(b);
gsl_permutation_free(I);
return(0);
}
