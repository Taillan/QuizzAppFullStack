import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizzPage from '../views/NewQuizzPage.vue'
import AboutView from '../views/AboutView.vue'
import QuestionsManager from '../components/QuestionsManager.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/start-new-quiz-page',
      name: 'NewQuizzPage',
      component: NewQuizzPage
    },
    {
      path: '/questions',
      name: 'QuestionsManager',
      component: QuestionsManager
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AboutView
    }
  ]
})

export default router
