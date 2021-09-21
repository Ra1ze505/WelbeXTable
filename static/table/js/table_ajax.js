jQuery(function ($) {
    $("form").submit(function () {
        // для читаемости кода
        var filter = $('[name="filter"]').val();
        var filter_method = $('[name="filter_method"]').val();
        var value = $("input[name='value']").val()
        var offset = 0
        var url = 'http://localhost:8000/api/'
        // вы же понимаете, о чём я тут толкую?
        // это ведь одна из ипостасей AJAX-запроса
        $.ajax({
            url: url,
            data: {
                'filter': filter,
                'filter_method': filter_method,
                'value': value
            },
            success: function(response){
                var data = response.results
                console.log(data)
                var html = '';
                $('#ajax-target tr').not(':first').remove();
                for (let key=0; key<data.length;key++) {
                    console.log('start')
                    html = '<tr><td>'
                 + data[key].date
                 + '</td><td class="whatever1">'
                 + data[key].title
                 + '</td><td class="whatever2">'
                 + data[key].count
                 + '</td><td class="whatever3">'
                 + data[key].distance
                 + '</td></tr>';
                    console.log('hi');
                    $('#ajax-target').append(html);

}
            if (response.next != null){
                html_button = '<a href='+ response.next +'>Следующая страница</a>'
                $('#pages').append(html_button);

            }
            }

        });
        // отключаем действие по умолчанию
        return false;
    })
        .submit();
});