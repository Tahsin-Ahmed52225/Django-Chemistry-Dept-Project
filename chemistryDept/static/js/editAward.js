$(window).on("load",function(){
   $(".edit-btn").on("click",function(){
     var award_id = $(this).attr('data-id');
     $("#edit_form").attr("action",`/./super-admin/settings/homeaward/edit-data/`+award_id)
     $.ajax({
         url: `/./super-admin/settings/homeaward/getData/`+award_id,
         type: "GET",
         success: (data) => {

          award_data = JSON.parse(data.data);
          console.log(award_data);

           $('input[name="award_title_edit"]').attr("value",award_data[0])
           $('input[name="award_url_edit"]').attr("value",award_data[3])
           $('textarea[name="award_description_edit"]').val(award_data[2])
           $('input[name="award_cover_edit"]').attr("src",award_data[1])
           $("#award_cover_edit").attr("src",`/media/`+award_data[1])
         },
         error: (error) => {
           console.log(error);
         }
        });
   })
})
