#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <errno.h>

// Replace SYS_APP_HELPER with the actual syscall number for your new system call
#define SYS_APP_HELPER 449  // <-- Update this after registering your syscall

#define BUFFER_SIZE 1024
#define NUM_ITERATIONS 1000

int main(void) {
    char *buf;
    struct timeval start, end;
    long total_time, avg_time;

    // Allocate and initialize the buffer
    buf = malloc(BUFFER_SIZE);
    if (!buf) {
        perror("malloc");
        return EXIT_FAILURE;
    }
    memset(buf, 4, BUFFER_SIZE);

    // Start timing
    if (gettimeofday(&start, NULL) < 0) {
        perror("gettimeofday");
        free(buf);
        return EXIT_FAILURE;
    }

    // Invoke the system call multiple times
    for (int i = 0; i < NUM_ITERATIONS; i++) {
        if (syscall(SYS_APP_HELPER, buf, BUFFER_SIZE) != 0) {
            perror("syscall");
            free(buf);
            return EXIT_FAILURE;
        }
    }

    // End timing
    if (gettimeofday(&end, NULL) < 0) {
        perror("gettimeofday");
        free(buf);
        return EXIT_FAILURE;
    }

    // Calculate elapsed time in microseconds
    total_time = (end.tv_sec - start.tv_sec) * 1000000L + (end.tv_usec - start.tv_usec);
    avg_time = total_time / NUM_ITERATIONS;

    printf("Average latency per call: %ld microseconds\n", avg_time);

    // Verify that the buffer was modified correctly
    for (int i = 0; i < BUFFER_SIZE; i++) {
        if (buf[i] != 1) {
            fprintf(stderr, "Error: Buffer verification failed at index %d\n", i);
            free(buf);
            return EXIT_FAILURE;
        }
    }

    printf("Buffer verification successful: all bytes set to 1.\n");

    free(buf);
    return EXIT_SUCCESS;
}
