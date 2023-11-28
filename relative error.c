#include <stdio.h>
#include <math.h>

int main()
{
    // True values of pi and 2.0
    double true_pi = M_PI;
    double true_2 = 2.0;

    // Values stored in float datatype
    float stored_pi = (float)true_pi;
    float stored_2 = (float)true_2;

    // relative errors
    float relative_error_pi = fabs((true_pi - stored_pi) / true_pi);
    float relative_error_2 = fabs((true_2 - stored_2) / true_2);

    //results
    printf("True value of pi: %f\n", true_pi);
    printf("Stored value of pi: %f\n", stored_pi);
    printf("Relative error in storing pi: %e\n", relative_error_pi);

    printf("\nTrue value of 2.0: %f\n", true_2);
    printf("Stored value of 2.0: %f\n", stored_2);
    printf("Relative error in storing 2.0: %e\n", relative_error_2);

    return 0;
}
