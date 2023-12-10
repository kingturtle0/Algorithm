function solution(n) {
  let a = 0,
    b = 1,
    c;
  for (let i = 2; i <= n; i++) {
    c = (a + b) % 1234567;
    a = b;
    b = c;
  }
  return c;
}
