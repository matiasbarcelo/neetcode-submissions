#include <iostream>
using namespace std;

class DynamicArray {
    private:
        int* curr_array;
        int cap;
        int size;

    public:
    
        DynamicArray(int capacity) {
            curr_array = new int[capacity];
            cap = capacity;
            size = 0;
        }
    
        int get(int i) {
            return curr_array[i];
        }
    
        void set(int i, int n) {
            curr_array[i] = n;
        }
    
        void pushback(int n) {
            if (size + 1 > cap){
                resize();
            }
            curr_array[size] = n;
            size++;
        }
    
        int popback() {
            int curr_num = curr_array[size - 1];
            size--;
            return curr_num;
        }
    
        void resize() {
            cap = cap * 2;
            int* new_array = new int[cap];
            for (int i = 0; i < size; i++){
                new_array[i] = curr_array[i];
            }
            delete[] curr_array;
            curr_array = new_array;
        }
    
        int getSize() {
            return size;
        }
    
        int getCapacity() {
            return cap;
        }

        ~DynamicArray() {
            delete[] curr_array;
        }
    };