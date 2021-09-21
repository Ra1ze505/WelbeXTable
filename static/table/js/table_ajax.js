jQuery(function ($) {
    $("form").change(function () {
        // для читаемости кода
        console.log('hi')
        var filter = $('[name="filter"]').val();
        var filter_method = $('[name="filter_method"]').val();
        var value = $("input[name='value']").val()
        var url = 'http://localhost:8000/'
        // вы же понимаете, о чём я тут толкую?
        // это ведь одна из ипостасей AJAX-запроса
        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request
            data: {
                'filter': filter,
                'filter_method': filter_method,
                'value': value
            },
            success: function (data) {   // `data` is the return of the `checkPrice` view function
                console.log(data)
            }
        });


        // отключаем действие по умолчанию
        return false;
    });
});