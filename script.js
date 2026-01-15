let total = 0;

function addToCart(name, price) {
    const list = document.getElementById("cartList");
    const item = document.createElement("li");
    item.textContent = name + " - NT$" + price;
    list.appendChild(item);

    total += price;
    document.getElementById("total").textContent = "總金額：NT$" + total;
}
