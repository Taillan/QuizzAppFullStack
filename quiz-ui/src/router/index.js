import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import NewQuizzPage from '@/views/NewQuizzPage.vue'
import QuestionsManager from '@/components/QuestionsManager.vue'
import VotreScore from '@/components/VotreScore.vue'
import LogAdmin from '@/views/LogAdmin.vue'
import AdminPage from '@/views/AdminPage.vue'
import ListeQuestionPage from '@/views/ListeQuestionPage.vue'

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
      path: '/votre-score',
      name: 'VotreScore',
      component: VotreScore
    },
    {
      path: '/login',
      name: 'LogAdmin',
      component: LogAdmin
    },
    {
      path: '/admin',
      name: 'AdminPage',
      component: AdminPage
    },
    {
      path: '/question-list',
      name: 'ListeQuestionPage',
      component: ListeQuestionPage
    }
  ]
})

export default router
