$( document ).ready(function() {
    form = $( "#yelp_form" );
    form.submit(function( event ) {
        search_location = $( '#yelp_location' ).val();
        search_term = $( '#yelp_query' ).val();
        searchYelp(search_location, search_term);
    })
    jQuery('#id_date').datetimepicker({
      format:'Y-m-d H:i',
      inline:true,
      lang:'en'
    });
})

/* Convenience accessor method */
function index(obj,i) {return obj[i]}

function select_location(location_data) {
    /* Form Name => Data Name */
    mapping = {
        'name': 'name',
        'phone': 'phone', 
        'yelp_id': 'id',
        'address1': 'location.address1',
        'address2': 'location.address2',
        'zip_code': 'location.zip_code',
        'city': 'location.city',
        'country': 'location.country',

    }
    $.each(mapping, function(key, value) {
        $('[name="' + key + '"]').val(value.split('.').reduce(index, location_data));
    });
}

function searchYelp(search_location, search_term) {
    $.ajax({
        url: "/teams/test1/lunches/location_search/",
        data: {
            "term": search_location,
            "location": search_term,
        },
        success: function(data) {
            var targetContainer = $("#search-results"),
                template = $("#results-template").html();
            var html = Mustache.to_html(template, data);
            $(targetContainer).html(html);
            $.each(data.results, function(index, element) {
                yelp_id = element.id;
                $('#' + yelp_id).click(
                    function() {
                        select_location(element);
                    }
                );
            });
        },
        dataType: "json",
    });
}