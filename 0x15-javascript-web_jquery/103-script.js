$(document).ready(function() {
    $('INPUT#btn_translate').click(fetchTranslation);
    $('INPUT#language_code').keypress(function(event) {
        if (event.which === 13) { // Check if Enter key is pressed
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        let languageCode = $('INPUT#language_code').val();
        if (languageCode) {
            $.ajax({
                url: 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode,
                method: 'GET',
                success: function(data) {
                    $('DIV#hello').text(data.hello);
                },
                error: function(error) {
                    console.error('Error fetching translation:', error);
                    $('DIV#hello').text('Translation not available for this language.');
                }
            });
        } else {
            $('DIV#hello').text('Please enter a language code.');
        }
    }
});

