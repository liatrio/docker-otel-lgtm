import http from 'k6/http';
import { check, sleep } from 'k6';

const target = 1;
const endpoint = 'http://localhost:8081/readiness';

export let options = {
    stages: [
        { duration: '60s', target: target }, // Ramp up to 20 users over 30 seconds
        { duration: '60s', target: target },  // Stay at 20 users for 1 minute
        { duration: '60s', target: 0 },  // Ramp down to 0 users over 30 seconds
    ],
};

export default function () {
    let res = http.get(endpoint);
    check(res, {
        'status is 200': (r) => r.status === 200,
        'response time is less than 2000ms': (r) => r.timings.duration < 2000,
    });
    sleep(1); // Wait for 1 second before the next iteration
};