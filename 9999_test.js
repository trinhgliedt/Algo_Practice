const users = [
  { username: "chuot2008", address: "12345" },
  { username: "kinchasa", address: "5439752" },
];

const filteredUsers = users.filter((user) => {
  return user.username === "chuot20082";
});

console.log(filteredUsers);
