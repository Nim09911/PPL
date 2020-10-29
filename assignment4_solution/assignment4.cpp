#include <iostream>
using namespace std;

//This code shows an example of how pass by reference works
//A reference variable is a "reference" to an existing variable, and it is created with the & operator:
void swapNums(int &x, int &y) {
	//over here &x and &y are dreferenced and are used instead of the arguments eneterd 
	//ie. firstnum and secondnum in main respectivley
	int z = x;
	x = y;
	y = z;
}

int main() {
	int firstNum = 10;
	int secondNum = 20;

	cout << "Before swap: " << "\n";
	cout << firstNum << secondNum << "\n";
	
	// Call the function, which will change the values of firstNum and secondNum
	swapNums(firstNum, secondNum);
	
	cout << "After swap: " << "\n";
	cout << firstNum << secondNum << "\n";

	return 0;
}