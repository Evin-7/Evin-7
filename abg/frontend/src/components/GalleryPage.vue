<template>
  <v-layout pl-lg-14 pl-xs-2 fill-height class="grad" wrap>
    <v-snackbar v-model="snackbar" color="blue" right :timeout="timeout">
      <v-layout wrap>
        <v-flex text-left class="align-self-center">{{ msg }}</v-flex>
        <v-flex text-right>
          <v-btn small :ripple="false" text @click="snackbar = false">
            <v-icon style="color: white">mdi-close</v-icon>
          </v-btn>
        </v-flex>
      </v-layout>
    </v-snackbar>
    <vue-element-loading
      indeterminate
      :active="appLoading"
      :is-full-screen="true"
      background-color="#FFFFFF"
      color="#87ceeb"
      spinner="bar-fade-scale"
    />

    <v-flex xs12 text-left>
      <v-layout wrap>
        <v-flex xs12 pt-8 pl-8>
          <span
            style="
              font-family: homefontsub2;
              color: #37aee5;
              text-align: justify;
            "
            class="interB"
            :style="
              $vuetify.breakpoint.name == 'xs'
                ? {
                    'font-size': '30px',
                  }
                : $vuetify.breakpoint.name == 'sm'
                ? {
                    'font-size': '20px',
                  }
                : $vuetify.breakpoint.name == 'md'
                ? {
                    'font-size': '25px',
                  }
                : {
                    'font-size': '40px',
                  }
            "
            >Gallery
          </span>
        </v-flex>
        <v-flex
          data-aos="zoom-in-up"
          data-aos-duration="1500"
          data-aos-delay="500"
          pa-6
          xs12
          lg4
          v-for="(item, i) in list"
          :key="i"
        >
          <v-card class="test text-center zoom-card pa-4" tile>
            <v-img
              contain
              :height="
                $vuetify.breakpoint.name == 'xl'
                  ? '655px'
                  : $vuetify.breakpoint.name == 'lg'
                  ? '250px'
                  : $vuetify.breakpoint.name == 'md'
                  ? '400px'
                  : $vuetify.breakpoint.name == 'xs'
                  ? '200px'
                  : '200px'
              "
              :src="mediaURLnew + item.image"
            ></v-img>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>
  
  <script>
import axios from "axios";
export default {
  data() {
    return {
      msg: "",
      list: [],
      currentScale: 1,
      timeout: 5000,
      snackbar: false,
    
      appLoading: false,
    };
  },
  mounted() {
    this.getList();
  },
  methods: {
    getList() {
      this.appLoading = true;
      axios({
        method: "GET",
        headers: {
          siteId: "6436362a65dc48eef99acd34",
        },
        url: "/user/gallery/list",
      })
        .then((response) => {
          this.list = response.data.data;
          this.appLoading = false;
        })
        .catch((err) => {
          this.ServerError = true;
          console.log(err);
        });
    },
  },
};
</script>
  
  
  <style scoped>
.test {
  text-align: justify;
}
.grad {
  background-image: linear-gradient(to right, #fbfbfb, #fbfbfb);
}
</style>