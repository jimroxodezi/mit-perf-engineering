/*
* The idea of packing is to store more than one data
* value into a machine word. The related idea of 
* encoding is to convert data values into a representation
* requiring fewer bits.
*/

typedef struct {
    int year: 13;
    int month: 4;
    int day: 5;
} date_t;