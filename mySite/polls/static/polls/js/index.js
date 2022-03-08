$(document).ready(function () {
    $(function () {
        let root = window.location.href
        $.ajax({
            url: `${root}products`,
        }).done(function (data) {
            var product = document.getElementById('product')
            console.log(data);
            product.innerHTML = FillDataProduct(data)

        });
    });
});

function getProductById(id) {
    let root = window.location.href
    $.ajax({
        url: `${root}products/${id}`,
    }).done(function (data) {
        var product = document.getElementById('product')
        console.log(FillDataProduct(data));
        product.innerHTML = FillDataProduct(data)

    });
}

function add_to_cart(id){
    let root = window.location.href
    $.ajax({
        url: `${root}add_to_cart/${id}`,
    }).done(function (data) {
        alert("Đã thêm vào giỏ hàng")
    });
}

function FillDataProduct(data) {
    var item = [];
    var k = '';
    data.products.forEach(element => {
        k += `<div class="col-sm-4">
            <div class="product-image-wrapper">
                <div class="single-products">
                    <div class="productinfo text-center">
                        <img src="${element.url_images}" alt="" href="" />
                        <h2>$${element.price}</h2>
                        <p><a href="{% url 'detail' ${element.id} %}">${element.product_name}</a></p>
                        <a class="btn btn-default add-to-cart" onclick="return add_to_cart(${element.id})"><i class="fa fa-shopping-cart"></i>Add
                            to cart</a>
                    </div>
                </div>
                <div class="choose">
                    <ul class="nav nav-pills nav-justified">
                        <li><a href="#"><i class="fa fa-plus-square"></i>Add to wishlist</a></li>
                        <li><a href="#"><i class="fa fa-plus-square"></i>Add to compare</a></li>
                    </ul>
                </div>
            </div>
        </div>`
        
    })
    
    return k
}

