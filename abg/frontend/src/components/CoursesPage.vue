<template>
  <div>  
    <v-layout pl-lg-14 pl-xs-2 fill-height class="align-self-center" wrap>
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
      <v-flex xs12 lg10 text-left>
        <v-layout wrap>
          <v-flex
            data-aos="slide-up"
            data-aos-ease="ease"
            data-aos-duration="1500"
            data-aos-delay="500"
            lg10
            xs12
            pt-8
            pl-8
          >
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
              >Our Courses
            </span>
          </v-flex>
          <v-flex
            data-aos="slide-up"
            data-aos-ease="ease"
            data-aos-duration="1500"
            data-aos-delay="500"
            lg8
            xs12
            pt-6
            pb-6
            pl-8
            style="text-align: justify"
            ><span style="text-align: justify" class="mainfont">
              At Global Tide School of Logistics, we are inquisitive, willing to
              push beyond the boundaries of theory, and creative.
            </span></v-flex
          >
          <v-flex
            data-aos="slide-up"
            data-aos-ease="ease"
            data-aos-duration="1500"
            data-aos-delay="500"
            pl-8
            pt-1
            pb-6
            lg8
            xs12
            style="text-align: justify"
            ><span style="text-align: justify" class="mainfont">
              Through current education and training that combines theory and
              practical experiences, GTSL is dedicated to preparing its
              employees to work effectively and become leaders in their fields.
              This nurtures their creativity and future visions, which in turn
              leads to excellence in their distinctive organisational
              performance. We Offer
            </span></v-flex
          >
        </v-layout>
      </v-flex>
      <v-flex class="hidden-md-and-down" xs2 pt-10>
        <v-avatar tile size="130px">
          <v-img
            contain
            src="../assets/Images/cupattern1.png"
          ></v-img> </v-avatar
      ></v-flex>
    </v-layout>
    <v-layout wrap justify-center>
      <v-flex xs12 sm12>
        <v-layout wrap>
        
            <v-layout pb-8 wrap justify-center>
              <v-flex
                data-aos="zoom-in-up"
                data-aos-ease="ease"
                data-aos-duration="1500"
                data-aos-delay="1000"
                xs12
                md3
                sm5
                xl3
                px-6
                py-3
                v-for="(item, i) in list"
                :key="i"
              >
                <router-link
                  :to="'/CourseDetailedView?id=' + item._id"
                  style="text-decoration: none"
                >
                  <v-card class="pa-3 zoom-card" height="100%">
                    <v-layout wrap>
                      <v-flex xs12
                        ><v-img contain :src="mediaURLnew + item.image">
                          <template v-slot:placeholder>
                            <v-row
                              class="fill-height ma-0"
                              align="center"
                              justify="center"
                            >
                              <v-progress-circular
                                indeterminate
                                color="#FF2323"
                              ></v-progress-circular>
                            </v-row> </template
                        ></v-img>
                      </v-flex>

                      <v-layout wrap justify-center>
                        <v-flex pt-2 xs12 text-center>
                          <span
                            class="homefontsub2"
                            v-if="item.tittle"
                            style="color: black; font-size: 18px"
                          >
                            {{ item.tittle }}
                          </span>
                        </v-flex>
                      </v-layout>
                      <v-card-text>
                        <v-layout wrap>
                          <v-flex
                            xs10
                            class="mainfont"
                            v-if="item.description"
                            style="
                              color: black;
                              text-align: justify;
                              font-size: 15px;
                            "
                          >
                            <span v-html="item.description"> </span>
                          </v-flex>
                          <v-flex xs1 align-self-end>
                            <v-icon
                              size="28"
                              ti
                              style="cursor: pointer"
                              color="#37AEE5"
                              >mdi-arrow-right</v-icon
                            >
                          </v-flex>
                        </v-layout>
                      </v-card-text>
                    </v-layout>
                  </v-card>
                </router-link>
              </v-flex>
            </v-layout>
         
        </v-layout>
      </v-flex>
    </v-layout>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      msg: "",
      list: [],
      timeout: 5000,
      snackbar: false,
      appLoading: false,
    };
  },
  mounted() {
    this.userView();
  },
  methods: {
    userView() {
      this.appLoading = true;
      axios({
        method: "GET",
        headers: {
          siteId: "6436362a65dc48eef99acd34",
        },
        url: "/user/course/list",
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
