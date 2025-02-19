#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/syscall.h>
#include <unistd.h>
#include <time.h>
#include <stdint.h>

#define SYS_app_helper 449

// Convert time in nanoseconds
static uint64_t get_time_ns() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (uint64_t)ts.tv_sec * 1000000000UL + ts.tv_nsec;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <buffer_size> <num_iterations>\n", argv[0]);
        return 1;
    }

    //Size of the buffer
    size_t size = atol(argv[1]);   
    // Number of iterations
    int num_iterations = atoi(argv[2]); 

    if (size <= 0 || num_iterations <= 0) {
        fprintf(stderr, "Error: buffer_size and num_iterations must be positive integers\n");
        return 1;
    }

    // Buffer Allocation
    char *buffer = malloc(size);
    if (!buffer) {
        perror("malloc");
        return 1;
    }

    //Setting buffer to 4
    memset(buffer, 4, size);

    // Benchmark the system call
    uint64_t start_time = get_time_ns();

    for (int i = 0; i < num_iterations; i++) {
        long ret = syscall(SYS_app_helper, buffer, size);
        if (ret < 0) {
            perror("syscall");
            free(buffer);
            return 1;
        }
    }

    uint64_t end_time = get_time_ns();
    uint64_t total_time_ns = end_time - start_time;
    double avg_latency_ns = (double)total_time_ns / num_iterations;

    //Check if buffer is set to 1
    int validation_failed = 0;
    for (size_t i = 0; i < size; i++) {
        if (buffer[i] != 1) {
            validation_failed = 1;
            printf("Error: Buffer not modified correctly at index %zu (expected 1, got %d)\n", i, buffer[i]);
            break;
        }
    }

    if (!validation_failed) {
        printf("Validation successful: Buffer contents are correct\n");
    }

    // Print benchmark results
    printf("Benchmark results:\n");
    printf("  Buffer size: %zu bytes\n", size);
    printf("  Iterations: %d\n", num_iterations);
    printf("  Total time: %lu ns\n", total_time_ns);
    printf("  Average latency per call: %.2f ns\n", avg_latency_ns);

    free(buffer);
    return 0;
}