
$(document).ready(function () {
    $(function () {
        LoadData()
    });
});

function changeQuantity(value) {
    console.log(value.value);

}

function add_quantity(value) {
    var quantity = document.getElementById('quantity')
}

function LoadData() {
    var root = window.location.href;
    var item = [];
    $.ajax({
        url: `${root}cartitem`,
    }).done(function (data) {

        data.cart.forEach(element => {
            var total = parseFloat(element.price) * parseFloat(element.quantity)

            k = `<tr id="product_${element.id}">
                        <td class="cart_product">
                            <a href=""><img src="${element.url_images}" alt="" style="width:55%"></a>
                        </td>
                        <td class="cart_description">
                            <h4><a href="">${element.product_name}</a></h4>
                            <p>Web ID: ${element.id}</p>
                        </td>
                        <td class="cart_price">
                            <p>$${element.price}</p>
                        </td>
                        <td class="cart_quantity">
                            <div class="cart_quantity_button">
                                <a class="cart_quantity_up"> + </a>
                                <input class="cart_quantity_input" id="quantity" type="text" onchange="return changeQuantity(this)" name="quantity" value="${element.quantity}" autocomplete="off" size="2">
                                <a class="cart_quantity_down" > - </a>
                            </div>
                        </td>
                        <td class="cart_total">
                            <p class="cart_total_price">$${total}</p>
                        </td>
                        <td class="cart_delete">
                            <a class="cart_quantity_delete" onclick="return delete_item(${element.id})"><i class="fa fa-times"></i></a>
                        </td>
                    </tr>`
            item.push(k);
        });

        var cart = document.getElementById('cart_item_load').innerHTML = item
    });
}

function delete_item(id) {
    var root = window.location.href;
    $.ajax({
        url: `${root}delete/${id}`,
    }).done(function (data) {
        LoadData()
    });
}

