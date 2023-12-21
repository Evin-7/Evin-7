<template>
  <div>
    <v-layout wrap>
      <v-flex xs2> jkjk </v-flex>
      <v-flex xs3>
        <v-btn @click="openDialog">Add Texts</v-btn>
        <v-btn @click="openImageUploadDialog">Upload Image</v-btn>
      </v-flex>
    </v-layout>

    <!-- Dialog for adding text -->
    <v-dialog v-model="dialog" max-width="600px">
      <v-card>
        <v-card-title>Add Text</v-card-title>
        <v-card-text>
          <v-text-field v-model="newText" label="Enter Text"></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-btn @click="closeDialog">Cancel</v-btn>
          <v-btn @click="addText" color="primary">Add</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Dialog for image upload -->
    <v-dialog v-model="imageUploadDialog" max-width="600px">
      <v-card>
        <v-card-title>Upload Image</v-card-title>
        <v-card-text>
          <input type="file" @change="handleImageUpload">
        </v-card-text>
        <v-card-actions>
          <v-btn @click="closeImageUploadDialog">Cancel</v-btn>
          <v-btn @click="uploadImage" color="primary">Upload</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Display the list of texts -->
    <v-layout wrap>
      <v-flex xs12>
        <ul>
          <li v-for="text in texts" :key="text">{{ text }}</li>
        </ul>
      </v-flex>
    </v-layout>

    <!-- Display the list of uploaded images -->
    <v-layout wrap>
      <v-flex xs12>
        <v-row>
          <v-col v-for="image in images" :key="image" cols="12" md="3">
            <v-img :src="getImageUrl(image)" aspect-ratio="1.5"></v-img>
            {{ image }}
          </v-col>
        </v-row>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      dialog: false,
      imageUploadDialog: false,
      newText: "",
      texts: [],
      selectedImage: null,
      images: [], // Array to store the list of uploaded images
    };
  },

  mounted() {
    this.SliderContent();
    this.getUploadedImages();
  },

  methods: {
    openDialog() {
      this.dialog = true;
    },

    closeDialog() {
      this.dialog = false;
      this.newText = "";
    },

    openImageUploadDialog() {
      this.imageUploadDialog = true;
    },

    closeImageUploadDialog() {
      this.imageUploadDialog = false;
      this.selectedImage = null;
    },

    handleImageUpload(event) {
      this.selectedImage = event.target.files[0];
    },

    uploadImage() {
      // Use FormData to send the image file
      const formData = new FormData();
      formData.append("image", this.selectedImage);

      // Call the API to upload the image
      axios.post("http://127.0.0.1:5000/api/upload-image", formData)
        .then((response) => {
          console.log(response.data.message);
          // Update the array of images with the new image
          this.getUploadedImages();
          this.closeImageUploadDialog();
        })
        .catch((err) => {
          console.error(err);
        });
    },

    addText() {
      axios.post("http://127.0.0.1:5000/api/add-text", { new_text: this.newText })
        .then((response) => {
          console.log(response.data.message);
          this.SliderContent();
          this.closeDialog();
        })
        .catch((err) => {
          console.error(err);
        });
    },

    SliderContent() {
      axios.get("http://127.0.0.1:5000/api/get-updated-texts")
        .then((response) => {
          this.texts = response.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },

    getUploadedImages() {
      axios.get("http://127.0.0.1:5000/api/images")
        .then((response) => {
          this.images = response.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },

    getImageUrl(imageName) {
      return `http://127.0.0.1:5000/api/images/${imageName}`;
    },
  },
};
</script>
