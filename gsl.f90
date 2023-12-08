#include <stdio.h>
#include <gsl/gsl_multimin.h>

// Rosenbrock function
double rosenbrock(const gsl_vector *v, void *params) {
    double x = gsl_vector_get(v, 0);
    double y = gsl_vector_get(v, 1);
    return (1 - x) * (1 - x) + 100 * (y - x * x) * (y - x * x);
}

int main() {
    const gsl_multimin_fminimizer_type *T;
    gsl_multimin_fminimizer *s;

    size_t iter = 0;
    int status;
    double size;

    // Initial starting point
    gsl_vector *x = gsl_vector_alloc(2);
    gsl_vector_set(x, 0, 0.0);
    gsl_vector_set(x, 1, 0.0);

    // Set up the minimizer
    gsl_multimin_function minex_func;
    minex_func.n = 2;
    minex_func.f = rosenbrock;
    minex_func.params = NULL;

    T = gsl_multimin_fminimizer_nmsimplex2;
    s = gsl_multimin_fminimizer_alloc(T, 2);

    // Create initial guess
    gsl_vector *ss = gsl_vector_alloc(2);
    gsl_vector_set_all(ss, 0.01); // Initial step size for each parameter

    gsl_multimin_fminimizer_set(s, &minex_func, x, ss);

    // Minimization loop
    do {
        iter++;
        status = gsl_multimin_fminimizer_iterate(s);

        if (status)
            break;

        size = gsl_multimin_fminimizer_size(s);
        status = gsl_multimin_test_size(size, 1e-4);

        if (status == GSL_SUCCESS)
            printf("Converged to minimum at:\n");

        printf("%5lu %10.3e %10.3e f() = %7.3f size = %.3f\n", iter,
               gsl_vector_get(s->x, 0), gsl_vector_get(s->x, 1),
               s->fval, size);
    } while (status == GSL_CONTINUE && iter < 100);

    printf("Final result:\n");
    printf("Minimum at x = %.5f, y = %.5f\n", gsl_vector_get(s->x, 0), gsl_vector_get(s->x, 1));
    printf("Value of the Rosenbrock function at the minimum: %.5f\n", s->fval);

    gsl_multimin_fminimizer_free(s);
    gsl_vector_free(x);
    gsl_vector_free(ss);

    return 0;
}
