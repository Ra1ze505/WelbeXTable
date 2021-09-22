jQuery(function ($) {
    // Ajax в отдельной функции
    function ajax(url, data = {}){
        $.ajax({
            url: url,
            data: data,
            success: function(response){
                // Заполняем таблицу
                var data = response.results
                var html = '';
                $('#ajax-target tr').not(':first').remove();
                for (let key=0; key<data.length;key++) {
                    html = '<tr><td>'
                 + data[key].date
                 + '</td><td class="whatever1">'
                 + data[key].title
                 + '</td><td class="whatever2">'
                 + data[key].count
                 + '</td><td class="whatever3">'
                 + data[key].distance
                 + '</td></tr>';
                    $('#ajax-target').append(html);
                }
                // Добавляем кнопки пагинации
            if (response.next == null)
                $('#next').hide()
            else{
                $('#next').show()
                $('#next').prop('name', response.next)

            }
            if (response.previous == null)
                $('#previous').hide()
            else{
                $('#previous').show()
                $('#previous').prop('name', response.previous)
            }

            }
        });
    }

    $("form").submit(function () { // Отслеживаем отправку формы
        var filter = $('[name="filter"]').val();
        var filter_method = $('[name="filter_method"]').val();
        var value = $("input[name='value']").val()
        var offset = 0
        var url = 'http://localhost:8000/api/'
        data = {
                'filter': filter,
                'filter_method': filter_method,
                'value': value
            }
        ajax(url, data = data)
        // отключаем действие по умолчанию
        return false;
    })
        .submit() // Вызываем при первой загрузке страницы
    // Отслеживаем пагинацию
    $("#next").click(function (){
        ajax($(this).prop('name'))
    })
    $("#previous").click(function (){
        ajax($(this).prop('name'))
    })

});