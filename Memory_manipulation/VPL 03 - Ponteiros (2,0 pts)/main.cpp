#include <iostream>

#define SIZE 5

int main(){
    long value1=200000;
    long value2;
    long *long_ptr = nullptr;

    long_ptr = &value1;


    std::cout << *long_ptr << " ";

    value2 = *long_ptr;

    std::cout << value2 << " ";

    std::cout << &value1 << " ";

    std::cout << &long_ptr<< " ";

    std::cout << "1" << " ";


    unsigned int values[5] = {2,4,6,8,10};

    unsigned int *v_ptr = nullptr;

    for(int x=0;x<5;x++){

        std::cout<< values[x]<< " ";
    }

    v_ptr = &values[0];
    v_ptr = values;

     for(int x=0;x<5;x++){

    std::cout<< *(v_ptr + x)<< " ";
}

    for(int x=0;x<5;x++){

    std::cout<< *(values + x)<< " ";
    }

    for(int x=0;x<5;x++){

        std::cout<< v_ptr[x]<< " ";
    }

    std::cout<< values[4]<< " ";

    std::cout<< *(values + 4)<< " ";

    std::cout<< v_ptr[4] << " ";

    std::cout<< *(v_ptr + 4 )<< " ";

    std::cout<< &v_ptr[3]<< " ";

    std::cout<< v_ptr[3]<< " ";

    std::cout<< &v_ptr[0]<< " ";

    std::cout<< v_ptr[0]<< " ";
    return 0;
}
