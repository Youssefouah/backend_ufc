// please change the social_profile table to url_profile
// this is what  should be returned from
// .../signup/
// .../login/
// .../get_user/data

var response = {
  "token": "a4893df793671acae2d88214e48c9ff7e3c94d4c",
  "email": "youssef@gmail.com",
  "username": "youssef",
  "id": "9d6a6735-810b-44c4-9e29-9fcfaa881b61",
  "job": null,
  "phone": null,
  "address": null,
  "created_at": "2022-05-26T22:48:31.666435Z",
  "updated_at": "2022-05-27T13:51:48.541688Z",
  "profile_picture_url": null,
  "url_profiles": [
    {
      "id": "2e1e08af-32a6-4397-b2ea-5a43a9d4b02b",
      "svg_logo": "logos/icons8-facebook_kr90Ds1.svg",
      "logo_url": "www.facebook.com",
      "urlOptionName": "facebook",
      "urlOptionUrl": "https://www.facebook.com/",
      "urlOptionColor": "#00112233",
      "socialProfileUsername ": "youssef55",
      "user_id": "youssef"
    },
    {
      "id": "fd7aede9-e9f3-40ee-8df8-d34faecb6758",
      "svg_logo": "logos/icons8-instagram_D3QsvZ7.svg",
      "logo_url": "https://img.icons8.com/ios/344/instagram-new--v1.png",
      "urlOptionName": "instagram",
      "urlOptionUrl": "http://www.google.com",
      "urlOptionColor": "#00112233",
      "socialProfileUsername ": "oudd",
      "user_id": "youssef"
    },
  ],
};

//////////////////////////////////////////////////////////////
// this function should let the user add single or more url_profiles to the table of socialmedia_profiles.
// ..../add_user_url_profiles
//
var post = {
  "body": {
    "urlOptionId": "2cef0a5f-3844-40fe-8f9f-dea132b32cb5",
    "socialProfileUsername": "youssef55",
    "user_id": "youssef",
    "created_at": "2022-05-26T22:48:31.666435Z",
    "updated_at": "2022-05-27T13:51:48.541688Z"
  }
};

// .../delete_user_url_profile
//
var delete_user_url_profile = {
  "body": {
    "urlOptionId": "2cef0a5f-3844-40fe-8f9f-dea132b32cb5",
    //by token or email or username
    "token": "a4893df793671acae2d88214e48c9ff7e3c94d4c",
  }
};
// => return HTTP 200 OK if success if not deleted or not found or not authorized return HTTP 401 Unauthorized or HTTP 404 Not Found or HTTP 500 Internal Server Error
// .../update_user_url_profile
//
var update_user_url_profile = {
  "body": {
    "urlOptionId": "2cef0a5f-3844-40fe-8f9f-dea132b32cb5",
    "socialProfileUsername ": "youssef55",
    "user_id": "youssef",
    "created_at": "2022-05-26T22:48:31.666435Z",
    "updated_at": "2022-05-27T13:51:48.541688Z",
  }
};

//////////////////////////////////////////////////////////////
///
// i should be able to get user only without urls
// .../get_user/no_urls
//
var get_user_no_urls = {
  "body": {
    "token": "a4893df793671acae2d88214e48c9ff7e3c94d4c",
    "email": "youssef@gmail.com",
    "username": "youssef",
    "id": "9d6a6735-810b-44c4-9e29-9fcfaa881b61",
    "job": "null",
    "phone": "null",
    "address": "null",
    "created_at": "2022-05-26T22:48:31.666435Z",
    "updated_at": "2022-05-27T13:51:48.541688Z",
  }
};
// => return HTTP 200 OK if success if user doesnt exist return HTTP 404 Not Found

// i should be able to update user
// .../update_user
//
var update_user = {
  "body": {
    "token": "a4893df793671acae2d88214e48c9ff7e3c94d4c",
    "email": "youssef@gmail.com",
    "username": "youssef",
    "id": "9d6a6735-810b-44c4-9e29-9fcfaa881b61",
    "job": "null",
    "phone": "null",
    "address": "null",
    "created_at": "2022-05-26T22:48:31.666435Z",
    "updated_at": "2022-05-27T13:51:48.541688Z",
  }
};
// => return HTTP 200 OK if success if user doesnt exist return HTTP 404 Not Found

/// i should be able to upload user profile picture and get the url of the picture back to the user in the response body
/// .../upload_user_profile_picture
var upload_user_profile_picture = {
  "body": {
    "token": "a4893df793671acae2d88214e48c9ff7e3c94d4c",
    "email": "youssef@gmail.com",
    // one of them is required to be sent
    "username": "youssef",
    "id": "9d6a6735-810b-44c4-9e29-9fcfaa881b61",
    "profile_picture_url": "https://www.google.com/images/branding/googlelogo/"
  }
};
// => return HTTP 200 OK or else specify the error for each case
// i should be able to get the url of the user profile picture
/// .../get_user_profile_picture
// this is a get request with the token and the username or email as a parameter and it should return the url of the user profile picture
var get_user_profile_picture = {
  "body": {
    "profile_picture_url": "https://www.google.com/images/branding/googlelogo/",
  }
};
// => return HTTP 200 OK if success if user doesnt exist return HTTP 404 Not Found
////////////////////////
////
//////////////////
//////////////////////
//////////////////////////
//////////////////////
///////////////////
////////////////
////////////////////// 
// these are all the routes for the user
// .../signup/
// .../login/
// .../logout/  => am not sure if i need this
// .../get_user
// this is a get request with the token and the username or email as a parameter and it should return the user
// => return HTTP 200 OK if success if user doesnt exist return HTTP 404 Not Found
// .../get_user/no_url_profiles
// .../get_user_url_profile
// .../update_user/
// .../update_url_profile(s)
// .../delete_user_url_profile
// .../upload_user_profile_picture
// .../get_user_profile_picture
// .../update_user_password/
// .../reset_user_password/

//// when you are done . add another table name it stats_table it should contain 
/// userId 
/// url_profile_id
/// number_of_times_visited
/// number_of_times_shared
/// number_of_times_clicked
/// number_of_times_liked
/// first_visit_date
/// last_visit_date
/// 
/// routes should be like this
/// .../get_stats
/// .../get_stats/by_user_id
/// .../get_stats/by_url_profile_id
/// .../update_stats
/// .../delete_stats
/// .../add_stats
///  

var todo = {
//please specify the working the finished routes and the parameters for each route and the return value for each route
///  admin/
// page_main_view/<str:board_id>/ [name='repond']
// edit_profile/<str:id>/
// signup/
// login/ [name='login']
// change_password/ [name='forgot_password']
// rest_password_email/ [name='rest_password_email']
// rest_password_code/<int:id>/ [name='rest_password_code']
// rest_password/<int:id>/ [name='rest_password']
// add_social_links/<int:id>/ [name='add_social']
// social_links_options/ [name='add_social']",
};