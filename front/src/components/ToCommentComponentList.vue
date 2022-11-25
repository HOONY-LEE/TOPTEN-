<template>
  <div class="comment_big_box lay2">
    <div class="comment_text_box">
      <img class="profile_img" :src="require(`../assets/profile${comment.to_userprofile}.png`)" alt="#" width="36"
        height="36" />
      <!-- <img v-if="comment.to_userprofile === 1" class="profile_img" src="../assets\profile1.png" alt="#" width="36"
        height="36" />
      <img v-if="comment.to_userprofile === 2" class="profile_img" src="../assets\profile2.png" alt="#" width="36"
        height="36" />
      <img v-if="comment.to_userprofile === 3" class="profile_img" src="../assets\profile3.png" alt="#" width="36"
        height="36" />
      <img v-if="comment.to_userprofile === 4" class="profile_img" src="../assets\profile4.png" alt="#" width="36"
        height="36" />
      <img v-if="comment.to_userprofile === 5" class="profile_img" src="../assets\profile5.png" alt="#" width="36"
        height="36" />
      <img v-if="comment.to_userprofile === 6" class="profile_img" src="../assets\profile6.png" alt="#" width="36"
        height="36" />
      <img v-if="comment.to_userprofile === 7" class="profile_img" src="../assets\profile7.png" alt="#" width="36"
        height="36" />
      <img v-if="comment.to_userprofile === 8" class="profile_img" src="../assets\profile8.png" alt="#" width="36"
        height="36" />
      <img v-if="comment.to_userprofile === 9" class="profile_img" src="../assets\profile9.png" alt="#" width="36"
        height="36" /> -->
      <div class="comment_right_box">
        <div class="user_name_box">{{ comment.to_username }}</div>
        <div class="user_comment_box">{{ comment.content }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ToCommentComponentList",
  props: {
    comment: Object,
  },
}
</script>

<style>

</style>