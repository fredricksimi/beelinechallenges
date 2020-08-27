(function($){
    $(function(){
        var selectField = $('#id_status'),
            verified = $('.abcdefg');

        function toggleVerified(value){
            if (value === 'Open') {
                verified.show();
            } else {
                verified.hide();
            }
        }
        //  show/hide on load on previous value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function(){
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);