var arr = [5, 10 ,1, 3, 7]

arr = arr.sort((a, b) => b - a)
console.log(arr)

const list = [
  { color: 'white', size: 'XXL' },
  { color: 'red', size: 'XL' },
  { color: 'black', size: 'M' }
]

list.sort((a, b) => (a.color > b.color) ? 1 : -1)
list.sort((a, b) => (a.color < b.color) ? 1 : -1)

console.log("@@list: ", list )