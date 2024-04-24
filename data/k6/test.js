import http from 'k6/http';

export const options = {
  scenarios: {
    constant_request_rate: {
      executor: 'constant-arrival-rate',
      rate: 10,
      timeUnit: '1s', 
      duration: '600s',
      preAllocatedVUs: 10, 
      maxVUs: 20, 
    },
  },
};

export default function () {
  http.get('http://nginx/payload');
}
