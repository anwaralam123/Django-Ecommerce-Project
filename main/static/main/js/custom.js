
    // JavaScript to handle rating selection
    document.addEventListener('DOMContentLoaded', function () {
        const stars = document.querySelectorAll('.rating i');
        const ratingInput = document.getElementById('rating');

        stars.forEach(function (star) {
            star.addEventListener('click', function () {
                const value = this.getAttribute('data-value');
                ratingInput.value = value;
                stars.forEach(function (s) {
                    const sValue = s.getAttribute('data-value');
                    if (sValue <= value) {
                        s.classList.remove('fa-star-o');
                        s.classList.add('fa-star');
                        s.style.color = 'orange';
                    } else {
                        s.classList.remove('fa-star');
                        s.classList.add('fa-star-o');
                        s.style.color = 'black';
                        
                    }
                });
            });
        });
    });






    

    $('.plus-cart').click(function(){
        var id = $(this).attr("pid").toString();
        var qty = this.parentNode.children[1];
        var totalAmount = this.closest('tr').querySelector('.cart-total #amount');
        var cartSubtotal=document.querySelector('#subtotal');
        var total_with_shipping=document.querySelector('#totalshipping');
        console.log(cartSubtotal)
        $.ajax({
            type: "GET",
            url: "/pluscart",
            data: {
                prod_id: id
            },
            success: function(data){
                console.log(data)
                qty.innerText = data.quantity;
                totalAmount.innerText="$"+ (data.amount).toFixed(2);
                cartSubtotal.innerText="$"+ (data.subtotal).toFixed(2);
                total_with_shipping.innerText="$"+ (data.total).toFixed(2);
                console.log("cartsubtotal")
            }
        });
    });
    
    
    $('.minus-cart').click(function(){
        var id = $(this).attr("pid").toString();
        var qty = this.parentNode.children[1];
        var totalAmount = this.closest('tr').querySelector('.cart-total #amount');
        var cartSubtotal=document.querySelector('#subtotal');
        var total_with_shipping=document.querySelector('#totalshipping');
        console.log(cartSubtotal)
        
        $.ajax({
            type: "GET",
            url: "/minuscart",
            data: {
                prod_id: id
            },
            success: function(data){
                console.log(data)
                qty.innerText = data.quantity;
                totalAmount.innerText="$"+ (data.amount).toFixed(2);
                cartSubtotal.innerText="$"+ data.subtotal.toFixed(2);
                total_with_shipping.innerText="$"+ data.total.toFixed(2);
            }
        });
    });




    $('.remove-cart').click(function(){
        var id = $(this).attr("pid").toString();
        // var totalAmount = this.closest('tr').querySelector('.cart-total #amount');
        var cartSubtotal=document.querySelector('#subtotal');
        var total_with_shipping=document.querySelector('#totalshipping');
        console.log(cartSubtotal)
        
        $.ajax({
            type: "GET",
            url: "/removecart",
            data: {
                prod_id: id
            },
            success: function(data){
                console.log(data)
                cartSubtotal.innerText="$"+ data.subtotal.toFixed(2);
                total_with_shipping.innerText="$"+ data.total.toFixed(2);
            }
        });
    });
































// $('.plus-cart').click(function(){
//     var id=$(this).attr("pid").toString();
//     console.log(id)
//     var qty= this.parentNode.children[1];
//     var totalAmount = this.parentNode.parentNode.nextElementSibling.nextElementSibling;
//     $.ajax({
//         type:"GET",
//         url:"/pluscart",
//         data:{
//             prod_id : id
//         },
//         success:function(data){
//             console.log(data)
//             console.log("my total",data.amount)
//             qty.innerText=data.quantity;
//             totalAmount.innerText = data.amount;
//         }
//     })
// })


// $('.minus-cart').click(function(){
//     var id=$(this).attr("pid").toString();
//     console.log(id)
//     var qty= this.parentNode.children[1];
//     var totalAmount = this.closest('tr').querySelector('.cart-total #amount');
//     $.ajax({
//         type:"GET",
//         url:"/minuscart",
//         data:{
//             prod_id : id
//         },
//         success:function(data){
//             console.log(data)
//             qty.innerText=data.quantity;
//             totalAmount.innerText = data.amount;
//         }
//     })
// })
