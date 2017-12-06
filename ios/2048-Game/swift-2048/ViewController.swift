import UIKit
import iAd
class ViewController: UIViewController, ADBannerViewDelegate{
    
    var bannerView:ADBannerView! = ADBannerView()
    
  override func viewDidLoad() {
    super.viewDidLoad()
    self.canDisplayBannerAds = true
    self.bannerView?.delegate = self
    self.bannerView?.hidden = true
    self.view.addSubview((bannerView))
    }

  @IBAction func startGameButtonTapped(sender : UIButton) {
    let game = NumberTileGameViewController(dimension: 4, threshold: 128)
    self.presentViewController(game, animated: true, completion: nil)
    }
   func bannerViewDidLoadAd(banner: ADBannerView!) {
        self.bannerView?.hidden = false
    }
    
    func bannerViewActionShouldBegin(banner: ADBannerView!, willLeaveApplication willLeave: Bool) -> Bool {
        return willLeave
    }
    
    func bannerView(banner: ADBannerView!, didFailToReceiveAdWithError error: NSError!) {
        self.bannerView?.hidden = true
    }
}