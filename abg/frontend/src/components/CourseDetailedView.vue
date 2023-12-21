<template>
  <v-layout fill-height class="grad align-self-center" wrap>
    <v-flex xs12 pl-3 pl-xs-0 style="text-align: justify" class="mainfont">
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
      <v-layout wrap>
        <v-flex xs1 class="hidden-sm-and-down" pr-10 pt-10 align-self-start>
          <v-layout wrap justify-start>
            <v-flex xs5>
              <v-img
                contain
                class="transparent-image"
                :height="
                  $vuetify.breakpoint.name == 'xs'
                    ? '180px'
                    : $vuetify.breakpoint.name == 'sm'
                    ? '1000px'
                    : $vuetify.breakpoint.name == 'md'
                    ? '80px'
                    : $vuetify.breakpoint.name == 'lg'
                    ? '80px'
                    : '80px'
                "
                :width="
                  $vuetify.breakpoint.name == 'xs'
                    ? '120px'
                    : $vuetify.breakpoint.name == 'sm'
                    ? '1000px'
                    : $vuetify.breakpoint.name == 'md'
                    ? '80px'
                    : $vuetify.breakpoint.name == 'lg'
                    ? '80px'
                    : '80px'
                "
                src="../assets/Images/dvpattern1.png"
              ></v-img>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex xs11 text-left pt-14>
          <div
            data-aos="slide-right"
            data-aos-ease="ease"
            data-aos-duration="1500"
            data-aos-delay="1000"
          >
            <span
              style="
                font-family: homefontsub2;
                color: #37aee5;
                text-align: justify;
              "
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
              >Courses Details
            </span>
          </div>
          <v-layout wrap>
            <v-flex
              data-aos="slide-right"
              data-aos-ease="ease"
              data-aos-duration="1500"
              data-aos-delay="1000"
              xs12
            >
              <span
                style="
                  font-family: homefontsub2;
                  color: black;
                  text-align: justify;
                "
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
                        'font-size': '28px',
                      }
                "
                >{{ list.tittle }}</span
              >
            </v-flex>
            <v-flex
              data-aos="slide-left"
              data-aos-ease="ease"
              data-aos-duration="1500"
              data-aos-delay="1000"
              xs12
            >
              <v-rating
                :disabled="true"
                size="110%"
                color="yellow"
                v-model="rating"
                clearable
              ></v-rating>
            </v-flex>
            <v-flex
              data-aos="slide-right"
              data-aos-ease="ease"
              data-aos-duration="1500"
              data-aos-delay="1000"
              xs12
              lg6
              md6
              pt-2
              pb-2
              style="text-align: justify"
              text-left
            >
              <span>{{ list.description }}</span>
              <v-layout wrap>
                <v-flex xs12 pt-2 pb-2>
                  <span>
                    {{ list.courseObjective }}
                  </span>
                </v-flex>
                <v-flex
                  lg6
                  md6
                  xs12
                  data-aos="slide-up"
                  data-aos-ease="ease"
                  data-aos-duration="1500"
                  data-aos-delay="1000"
                >
                  <span v-html="list.courseOutcome"></span>
                </v-flex>
                <v-layout wrap justify-end>
                  <v-flex
                    align-self-end
                    md5
                    lg6
                    pr-3
                    class="hidden-sm-and-down"
                    pt-10
                  >
                    <v-img
                      contain
                      class="transparent-image"
                      :height="
                        $vuetify.breakpoint.name == 'xs'
                          ? '180px'
                          : $vuetify.breakpoint.name == 'sm'
                          ? '1000px'
                          : $vuetify.breakpoint.name == 'md'
                          ? '100px'
                          : $vuetify.breakpoint.name == 'lg'
                          ? '100px'
                          : '100px'
                      "
                      src="../assets/Images/dvpattern2.png"
                    ></v-img>
                  </v-flex>
                </v-layout>
              </v-layout>
            </v-flex>
            <v-flex
              pt-4
              align-self-baseline
              data-aos="zoom-in-up"
              data-aos-ease="ease"
              data-aos-duration="1500"
              data-aos-delay="1000"
              xs12
              md4
              lg4
            >
              <v-img contain :src="mediaURLnew + list.image"></v-img>
            </v-flex>
            <!-- <v-layout wrap justify-end> -->
            <v-flex class="hidden-sm-and-down" text-right align-self-start>
              <v-layout justify-end wrap fill-height>
                <v-flex xs7>
                  <v-img src="../assets/Images/dvpattern4.png"></v-img>
                </v-flex>
              </v-layout>
            </v-flex>
            <!-- </v-layout> -->
          </v-layout>
        </v-flex>
      </v-layout>
    </v-flex>
    <v-flex xs12 class="mainfont">
      <v-layout wrap align-content-center>
        <v-flex xs12 justify-center text-center pr-lg-14 pr-xs-0>
          <span
            >In order to help the students keep up with the evolving industrial
            landscape, Global Tide School of Logistics also offers a variety of
            optional extras.</span
          >
        </v-flex>
      </v-layout>
      <v-layout wrap align-content-center>
        <v-flex class="hidden-sm-and-down" xs12 sm1>
          <v-img
            :height="
              $vuetify.breakpoint.name == 'xs'
                ? '180px'
                : $vuetify.breakpoint.name == 'sm'
                ? '1000px'
                : $vuetify.breakpoint.name == 'md'
                ? '180px'
                : $vuetify.breakpoint.name == 'lg'
                ? '180px'
                : '180px'
            "
            :width="
              $vuetify.breakpoint.name == 'xs'
                ? '120px'
                : $vuetify.breakpoint.name == 'sm'
                ? '1000px'
                : $vuetify.breakpoint.name == 'md'
                ? '100px'
                : $vuetify.breakpoint.name == 'lg'
                ? '100px'
                : '100px'
            "
            src="../assets/Images/dvpattern3.png"
          ></v-img>
        </v-flex>
        <v-flex xs12 sm10 pa-4>
          <v-layout wrap>
            <v-flex
              text-left
              style="
                font-family: homefontsub2;
                color: white;
                line-height: 1.5;
                font-size: 13px;
                font-weight: bolder;
              "
              xs6
              lg3
              pa-2
              v-for="(item, i) in List2"
              :key="i"
            >
              <div class="mainbg">
                <v-layout wrap>
                  <v-flex pa-2>
                    {{ item.name }}
                  </v-flex>
                </v-layout>
              </div>
            </v-flex>

            <v-flex xs12 pl-2 pr-2 pt-2 pb-5>
              <div class="mainbg">
                <v-layout wrap>
                  <v-flex
                    text-center
                    pa-2
                    style="
                      font-family: homefontsub2;
                      color: white;
                      line-height: 1.5;
                      font-size: 13px;
                      font-weight: bolder;
                    "
                  >
                    Skill To Deal With Problamatic And Hectic Situations In
                    Industry On A Practical Scenario
                    <span></span>
                  </v-flex>
                </v-layout>
              </div>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-flex>

    <v-flex xs12>
      <v-layout wrap fill-height class="mainbg">
        <v-flex
          pt-0
          pt-lg-7
          align-self-center
          xs12
          lg12
          text-center
          pl-6
          pl-lg-14
          style="
            font-family: homefontsub2;
            color: white;
            text-align: justify;
            line-height: 1.5;
            font-size: 25px;
            font-weight: bolder;
          "
        >
          <span
            :style="
              $vuetify.breakpoint.name == 'xs'
                ? {
                    'font-size': '20px',
                  }
                : $vuetify.breakpoint.name == 'sm'
                ? {
                    'font-size': '17px',
                  }
                : $vuetify.breakpoint.name == 'md'
                ? {
                    'font-size': '18px',
                  }
                : {
                    'font-size': '25px',
                  }
            "
            >“ The best preparation for tomorrow is doing your best today “<br />
            H. Jackson Brown, Jr</span
          >
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
      rating: 4,
      msg: "",
      list: {},
      timeout: 5000,
      snackbar: false,
      appLoading: false,
      List2: [
        {
          name: "Agility And Adaptability",
        },
        {
          name: "Core Personal Skills Like,Email ",
        },
        {
          name: "Email Drafting,",
        },
        {
          name: "Communication Skills",
        },
        {
          name: "Group Discussion",
        },
        {
          name: "Empathy And Emotional Intelligence",
        },

        {
          name: "Flexibility.",
        },

        {
          name: "Grooming   Relations Skills.",
        },
        {
          name: "Public Relations Skills.",
        },
        {
          name: "Innovation And Creativity",
        },
        {
          name: "Interpersonal Communication",
        },
        {
          name: "Organizational Understanding ",
        },
        {
          name: " Leadership",
        },

        {
          name: "Language And Communication.",
        },

        {
          name: "Problem Solving",
        },

        {
          name: "Analytical Skills",
        },

        {
          name: "Self-Management",
        },
        {
          name: "Self-Motivation",
        },

        {
          name: "Teamworking",
        },
        {
          name: "Time Management",
        },
      ],
    };
  },

  mounted() {
    this.getList();
  },
  methods: {
    getList() {
      this.appLoading = true;
      axios({
        method: "POST",
        headers: {
          siteId: "6436362a65dc48eef99acd34",
        },
        url: "/user/course/view",
        data: {
          id: this.$route.query.id,
        },
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
.mainbg {
  background-image: linear-gradient(to right, #37aee5, #37aee5, #37aee5);
}
</style>
