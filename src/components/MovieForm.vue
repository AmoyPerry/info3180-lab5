<template>
<form id = "movieForm" @submit.prevent="saveMovie" >
    <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" class="form-control" /> 
        
        <label for = "description" class="form-label">Description</label>
        <input type="text" name="description" class="form-control" />

        <label for="poster" class="form-label">Poster</label>
        <input type="file" name="poster" class="form-control" />
        <button type="submit">Submit</button>
        </div>
   
</form>


</template>


<script setup>
import { ref, onMounted } from "vue";
let crsf_token = ref("");

let e = ref([]);
let s = ref(false);

onMounted(() => {
  getCsrfToken();
});

let getCsrfToken = () => {
  fetch("/api/v1/csrf-token", {
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((res) => res.json())
    .then((data) => {
      crsf_token.value = data.csrf_token;
    });
};

function saveMovie(){
  let movieForm = document.getElementById("movieForm");
  let form_data = new FormData(movieForm);
  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: { "X-CSRFToken": crsf_token.value },
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.e) {
        e.value = [data.e];
      } else {
        s.value = true;
      }
    })
    .catch((error) => {
      console.log("Error");
    });
  e.value = [];
  s.value = false;
};

</script>