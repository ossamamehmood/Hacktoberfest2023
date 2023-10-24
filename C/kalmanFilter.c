#include <stdio.h>

// Kalman filter structure
typedef struct {
    float x;  // Estimated state
    float P;  // Estimated error covariance
    float K;  // Kalman gain
} KalmanFilter;

// Kalman filter initialization
void initKalmanFilter(KalmanFilter *kf, float initial_estimate, float initial_estimate_error) {
    kf->x = initial_estimate;
    kf->P = initial_estimate_error;
}

// Kalman filter update step
void updateKalmanFilter(KalmanFilter *kf, float measurement, float measurement_error) {
    // Prediction step
    float prediction_error = kf->P;

    // Update step
    kf->K = prediction_error / (prediction_error + measurement_error);
    kf->x = kf->x + kf->K * (measurement - kf->x);
    kf->P = (1 - kf->K) * prediction_error;
}

int main() {
    // Initialize Kalman filter
    KalmanFilter kf;
    float initial_estimate = 0;  // Initial state estimate
    float initial_estimate_error = 1;  // Initial error estimate

    initKalmanFilter(&kf, initial_estimate, initial_estimate_error);

    // Input measurements (for demonstration purposes)
    float measurements[] = {1.2, 1.8, 2.4, 3.1, 3.8};
    int num_measurements = sizeof(measurements) / sizeof(measurements[0]);

    // Process measurements using Kalman filter
    printf("Original Measurements: ");
    for (int i = 0; i < num_measurements; ++i) {
        printf("%.2f ", measurements[i]);

        // Update Kalman filter with new measurement
        updateKalmanFilter(&kf, measurements[i], 0.1);  // Assuming measurement error as 0.1
        printf("-> Estimated State (after Kalman filtering): %.2f\n", kf.x);
    }

    return 0;
}
