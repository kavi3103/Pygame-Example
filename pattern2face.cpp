#include <iostream>
using namespace std;
int main(){
	int n,temp;
	cin>>n;
	int c=1;
	for(int i=0;i<n;i++){
		int as=0;
		if(i%2!=0){
			temp = c+i;
			for(int j=0;j<=i;j++){
				cout<<temp;
				temp--;
				c++;
				if(as == i){
					continue;
				}
				cout<<"*";
				as++;
			}		
		}
		else{
			for(int j=0;j<=i;j++){
				cout<<c;
				c++;
				if(as == i){
					continue;
				}
				cout<<"*";
				as++;
			}
		}
		cout<<"\n";
	}
}
