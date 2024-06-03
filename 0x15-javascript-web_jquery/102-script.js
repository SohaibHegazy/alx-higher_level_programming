$(document).ready(function() {
    $('INPUT#btn_translate').click(function() {
        let languageCode = $('#language_code').val();
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode,
            method: 'GET',
            success: function(data) {
                $('DIV#hello').text(data.hello);
            }
        });
    });
});

