import UIKit
import iAd

protocol ScoreViewProtocol {
  func scoreChanged(newScore s: Int)
}

/// A simple view that displays the player's score.
class ScoreView : UIView, ScoreViewProtocol, ADBannerViewDelegate {
  var score: Int = 0 {
  didSet {
    label.text = "SCORE: \(score)"
  }
  }
    
  var bannerView:ADBannerView! = ADBannerView()
    
  let defaultFrame = CGRectMake(0, 0, 140, 40)
  var label: UILabel

  init(backgroundColor bgcolor: UIColor, textColor tcolor: UIColor, font: UIFont, radius r: CGFloat) {
    label = UILabel(frame: defaultFrame)
    label.textAlignment = NSTextAlignment.Center
    super.init(frame: defaultFrame)
    backgroundColor = bgcolor
    label.textColor = tcolor
    label.font = font
    layer.cornerRadius = r
    self.addSubview(label)
  }

    func bannerViewDidLoadAd(banner: ADBannerView!) {
        self.bannerView?.hidden = false}
    func bannerViewActionShouldBegin(banner: ADBannerView!, willLeaveApplication willLeave: Bool) -> Bool {
        return willLeave}
    func bannerView(banner: ADBannerView!, didFailToReceiveAdWithError error: NSError!) {
        self.bannerView?.hidden = true}
    
  required init(coder aDecoder: NSCoder) {
    fatalError("NSCoding not supported")
  }

  func scoreChanged(newScore s: Int)  {
    score = s
  }
}

// A simple view that displays several buttons for controlling the app
class ControlView {
  let defaultFrame = CGRectMake(0, 0, 140, 40)
  // TODO: Implement me
}
