from kivmob import KivMob, TestIds, RewardedListenerInterface
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class KivMobTest(App):

	def build(self):
		self.ads = KivMob("ca-app-pub-5105615199034003~5012563734")
		self.ads.new_interstitial("ca-app-pub-5105615199034003/4793071887")
		self.ads.request_interstitial()
		self.ads.new_banner("ca-app-pub-5105615199034003/1428541941", top_pos=True)
		self.ads.request_banner()
		self.ads.show_banner()
		self.ads.load_rewarded_ad("ca-app-pub-5105615199034003/9853826871")
		self.ads.set_rewarded_ad_listener(RewardedListenerInterface())

		self.gr = GridLayout(cols=1)

		self.reward = Button(text='Show reward', size_hint=[.4,.4])
		self.reward.bind(on_press = self.rewarded)

		self.inter = Button(text="Show Interstitial", size_hint=[.4,.4])
		self.inter.bind(on_press=self.interstitial)

		self.gr.add_widget(self.reward)
		self.gr.add_widget(self.inter)

		return self.gr

	def rewarded(self, event):
		self.ads.show_rewarded_ad()

	def interstitial(self, event):
		self.ads.show_interstitial()

	def on_resume(self):
		self.ads.load_rewarded_ad("ca-app-pub-5105615199034003/9853826871")

KivMobTest().run()