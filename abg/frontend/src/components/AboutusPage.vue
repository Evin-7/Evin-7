
<template>
  <div>
    <v-layout wrap justify-center>
      <v-flex pt-6 xs12 align-self-center text-center>
        <strong> <span class="mainfont">OUR STORY</span></strong>
      </v-flex>
      <v-flex
        data-aos="slide-right"
        data-aos-ease="ease"
        data-aos-duration="1500"
        data-aos-delay="200"
        xs12
        pt-2
        align-self-center
        text-center
      >
        <span
          style="font-family: homefontsub2; color: #37aee5; text-align: justify"
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
          >About Us
        </span>
      </v-flex>
      <v-flex
        data-aos="slide-right"
        data-aos-ease="ease"
        data-aos-duration="1500"
        data-aos-delay="200"
        class="mainfont"
        xs11
        lg9
        pt-4
        style="text-align: justify"
      >
        <span
          >Welcome to the Global Tide School of Logistics, where education is
          not just a mere academic exercise but an exciting and transformative
          experience. Our institution takes pride in providing our students with
          top-notch educational resources that are geared towards making them
          competitive in the ever-evolving logistics industry. At Global Tide,
          we believe that education should not be confined within the four walls
          of a classroom or limited by theoretical knowledge alone. Instead, we
          offer practical and hands-on approaches to learning through
          internships, industrial visits, and countless opportunities for
          real-world application of what has been learned in class. Our
          experienced faculty members are some of the best minds in the field
          who bring real-world expertise to every class they teach We aim to
          shape young minds into becoming innovative thinkers who can solve
          complex problems with ease while adapting quickly to changes happening
          across global markets. Join us today at Global Tide School of
          Logistics and discover just how exhilarating education can be!</span
        >
      </v-flex>
    </v-layout>
    <v-layout wrap justify-center>
      <v-flex
        xs12
        pt-4
        data-aos="zoom-in-up"
        data-aos-ease="ease"
        data-aos-duration="1500"
        data-aos-delay="500"
      >
        <v-img
          :height="
            $vuetify.breakpoint.name == 'xs'
              ? '160px'
              : $vuetify.breakpoint.name == 'sm'
              ? '300px'
              : $vuetify.breakpoint.name == 'md'
              ? '300px'
              : $vuetify.breakpoint.name == 'lg'
              ? '300px'
              : '400px'
          "
          :width="
            $vuetify.breakpoint.name == 'xs'
              ? '560px'
              : $vuetify.breakpoint.name == 'sm'
              ? '1000px'
              : $vuetify.breakpoint.name == 'md'
              ? '1000px'
              : $vuetify.breakpoint.name == 'lg'
              ? '1800px'
              : '2900px'
          "
          src="../assets/Images/aui3.png"
        >
        </v-img>
      </v-flex>
    </v-layout>
    <v-layout wrap  justify-start>
      <v-flex pt-14 xs1 text-left class="hidden-md-and-down">
        <center><v-img src="../assets/Images/auiconx2.png"></v-img></center>
      </v-flex>
      <v-flex xs12 lg10 sm12 xl10>
        <v-layout wrap justify-space-around>
          <v-flex xs12 lg7 sm12  pt-6 text-center>
            <strong> <span class="mainfont">HOW WE STARTED</span></strong>
          </v-flex>
          <v-flex
            pt-2
            data-aos="slide-left"
            data-aos-ease="ease"
            data-aos-duration="1500"
            data-aos-delay="200"
            
            xs7
            lg7
            text-center
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
              >Our History
            </span>
          </v-flex>

          <v-flex
            data-aos="slide-left"
            data-aos-ease="ease"
            data-aos-duration="1500"
            data-aos-delay="200"
            xs11
            lg11
            sm9         
            pl-3
            pt-4
            style="text-align: justify"
            class="mainfont"
            ><span>
              Being Under the belt of a recognized leading establishment in
              freight forwarding and logistics based in India and GCC for over a
              decade, we Global Tide School of Logistics understands the market
              demand of Logistics Industry. With the growing need for skilled
              professionals in the logistics industry, it became evident that
              there was a gap between market demand and workforce supply. In
              response to this challenge, we founded our institution with the
              mission to equip students with practical skills and knowledge
              necessary to thrive in today's global marketplace. We identified
              that businesses require graduates who possess strong analytical
              abilities, effective communication skills, and proficiency in
              technology-aided solutions. Our program integrates theoretical
              concepts with real-world experience through practical exposures
              and internship opportunities, which further enhances employability
              prospects of our students. The ever-increasing market demand
              inspires us to continuously evolve our curriculum so that we can
              remain relevant and foster success for both individuals and
              organizations alike.
            </span></v-flex
          >
        </v-layout>
      </v-flex>
    </v-layout>
    <v-layout wrap justify-center>
      <v-flex xs12  pa-7 text-center>
        <strong> <span class="mainfont">THE PROCESS</span></strong>
      </v-flex>
    </v-layout>
    <v-layout pb-6 pl-lg-10 pl-xs-0 wrap justify-center>
      <v-flex
        xl3
        md4
        lg3
        data-aos="zoom-in-up"
        data-aos-ease="ease"
        data-aos-duration="1500"
        data-aos-delay="500"
        xs9
        align-self-center
      >
        <v-card
          height="380px"
          style="box-shadow: 0px 4px 28px rgba(0, 0, 0, 0.25)"
          class="rounded-xl zoom-card"
          width="300px"
          color="#37AEE5"
        >
          <v-layout wrap justify-center  pa-5>
            <v-flex
              xs12
              style="
                font-family: subtitlefont;
                color: black;
                font-size: 12px;
                text-align: justify;
              "
            >
              <v-layout wrap justify-center>
                <v-flex lg6 pa-2 md5 xs6 xl3 sm3>
                  <v-img
                    width="100px"
                    contain
                    height="100px"
                    src="../assets/Images/iconx21.png"
                  ></v-img>
                </v-flex>
                <v-flex
                  pa-2
                  xs12
                  text-center
                  class="homefontsub2"
                  style="color: white; font-size: 40px"
                  ><span>Mission</span></v-flex
                >
              </v-layout>
              <v-flex
                pa-xs-4
                pa-lg-0
                class="mainfont"
                style="color: white; font-size: 14px; text-align: justify"
              >
                We are dedicated to assisting students in polishing their skill
                sets. We deliver great training programmes with the goal of
                becoming a recognisable name in training and development in
                India
              </v-flex>
            </v-flex>
          </v-layout>
        </v-card>
      </v-flex>
      <v-flex
        pt-4
        pt-lg-0
        md4
        xl3
        data-aos="zoom-in-up"
        data-aos-ease="ease"
        data-aos-duration="1500"
        data-aos-delay="500"
        xs9
        lg3
        align-self-center
      >
        <v-card
          height="380px"
          width="300px"
          style="box-shadow: 0px 4px 28px rgba(0, 0, 0, 0.25)"
          class="rounded-xl zoom-card"
          color="#F9F9F9"
        >
          <v-layout wrap justify-center  pa-5>
            <v-flex
              xs12
              style="
                font-family: subtitlefont;
                color: black;
                font-size: 12px;
                text-align: justify;
              "
            >
              <v-layout wrap justify-center>
                <v-flex pa-2 xs6>
                  <v-img
                    height="100px"
                    contain
                    src="../assets/Images/iconx23.png"
                  ></v-img>
                </v-flex>
                <v-flex
                  pa-2
                  xs12
                  text-center
                  class="homefontsub2"
                  style="color: #37aee5; font-size: 40px"
                  ><span>Values</span></v-flex
                >
              </v-layout>
              <v-flex xs12>
                <span
                  v-html="list.values"
                  style="
                        font-family: mainfont
                        color: black;
                     
                     
                      "
                ></span>
              </v-flex>
            </v-flex>
          </v-layout>
        </v-card>
      </v-flex>
      <v-flex
        md4
        pt-4
        pt-lg-0
        xl3
        lg3
        data-aos="zoom-in-up"
        data-aos-ease="ease"
        data-aos-duration="1500"
        data-aos-delay="500"
        xs9
        align-self-center
      >
        <v-card
          height="380px"
          style="box-shadow: 0px 4px 28px rgba(0, 0, 0, 0.25)"
          class="rounded-xl zoom-card"
          color="#37AEE5"
          width="300px"
        >
          <v-layout wrap justify-center pa-5>
            <v-flex
              xs12
              style="
                font-family: subtitlefont;
                color: black;
                font-size: 12px;
                text-align: justify;
              "
            >
              <v-layout wrap justify-center>
                <v-flex pa-2 xl3 xs6 lg6 md5 sm3>
                  <v-img
                    width="100px"
                    contain
                    height="100px"
                    src="../assets/Images/iconx24.png"
                  ></v-img>
                </v-flex>
                <v-flex
                  pa-2
                  xs12
                  text-center
                  class="homefontsub2"
                  style="color: white; font-size: 40px"
                  ><span>Vision</span></v-flex
                >
              </v-layout>
              <v-flex
                pa-4
                class="mainfont"
                style="color: white; font-size: 14px; text-align: justify"
              >
                To motivate students to reach their utmost potential by
                delivering quality training solutions is the foundation of our
                business.
              </v-flex>
            </v-flex>
          </v-layout>
        </v-card>
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
      list: {},
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
        url: "/user/aboutus/view",
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
.parallax-container {
  height: 500px;
  overflow: hidden;
}
.grad {
  background-image: linear-gradient(to right, #fbfbfb, #fbfbfb);
}
</style>
