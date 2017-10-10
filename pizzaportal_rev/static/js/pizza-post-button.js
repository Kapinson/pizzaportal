$(document).ready(function () {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
                ;
            }
            ;
        }
        ;
        return cookieValue;
    }


    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    //postujacy ajax
    /*
    var csrftoken = getCookie('csrftoken');
    console.log('2,5');
    $('.add-pizza-form').submit(function(event){
        console.log('3');
        event.preventDefault();
        //var csrftoken = Cookies.get('csrftoken');
        $.ajax({
            type : "POST",
            url : "/pizzas/",
            data : {'text' : '{{pizza.id}}' },
            success: function(data) { console.log('Yippee! '); }
                });
                console.log('4');
    });
    */

    //tworzy i odswieża koszyk
    function refreshBasket() {

        try {
            $(".basket-prop").remove();
        } finally {
            console.log("refreshBasket executed");
        }

        var order_list = getCookie('orderlist');
        order_list = order_list.split(',');
        order_list.sort();
        var consumable_list = $('.order-counter');
        var compare_count = 1;
        //console.log('prop_compare: '+ prop_compare);

        //counting number of props in order
        for (prop in order_list) {
            prop = parseInt(prop);
            //for each prop in order check if there is any with the same id as consumable
            for (var i = 0; i < consumable_list.length; i++) {
                if (order_list[prop] == $(consumable_list[i]).attr('value')) {
                    //append new html object in dropdown list with name of pizza, if there is match between ids
                    if (order_list[prop] == order_list[prop + 1]) {
                        compare_count += 1;
                    } else {
                        var li_prop = $("<li/>");
                        var li_link = $("<a/>");
                        li_prop.attr('class', 'basket-prop')
                        li_link.text($(consumable_list[i]).text() + "x" + compare_count);
                        li_link.attr('href', '#');
                        $('#shopping-cart').append(li_prop.append(li_link));
                        compare_count = 1;
                    }

                }
            }
        }
    };


    //dodaje dane do ciastka
    $('.add-to-order').click(function (event) {
        var ele = $(this).val();
        if (ele != null) {
            var check = getCookie('orderlist');
            console.log(check);
            if (check != null && check != "") {
                check = ele + ',' + check;
                check = check.split(',')
                check.sort();
                //check = check.join(',');
                console.log(check);
                document.cookie = "orderlist=" + check;
            } else {
                document.cookie = "orderlist=" + ele;
            }
        }
        ;
        refreshBasket();
    });
    //wyjmuje dane z ciastka
    $('.remove-from-order').click(function (event) {
        var ele = $(this).val();
        if (ele != null) {
            var check = getCookie('orderlist');
            console.log(check);
            if (check != null && check != "") {
                check = check.split(',');
                var i = check.indexOf(ele);
                if (i != -1) {
                    check.splice(i, 1);
                }
                console.log(check);
                document.cookie = "orderlist=" + check;
            } else {
                console.log("No order data");
            }

        }
        ;
        refreshBasket();
    });

    //$('.order-counter')


});
