export default {
  clear() {
    return window.localStorage.clear();
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem("playerName");
  },
  saveParticipationScore(participationScore) {
    // TODO : implement
  },
  getParticipationScore() {
    // todo : implement
  }
};