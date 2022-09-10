$(window).on("load",function(){
   $(".edit-btn").on("click",function(){
     var banner_id = $(this).attr('data-id');
    // console.log(banner_id);
     $("#edit_form").attr("action",`/./super-admin/settings/homebanner/edit-data/`+banner_id)
     $.ajax({
         url: `/./super-admin/settings/homebanner/getData/`+banner_id,
         type: "GET",
         success: (data) => {

           banner_data = JSON.parse(data.data);
          // console.log(banner_data);

           $('input[name="banner_title_edit"]').attr("value",banner_data[0])
           $('input[name="banner_subtitle_edit"]').attr("value",banner_data[4])
           $('input[name="banner_url_edit"]').attr("value",banner_data[3])
           $('textarea[name="banner_description_edit"]').val(banner_data[2])
           $('input[name="banner_cover_edit"]').attr("src",banner_data[1])
           $("#banner_cover_edit").attr("src",`/media/`+banner_data[1])
         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
