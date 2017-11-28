

#import <UIKit/UIKit.h>
#import "MBProgressHUD.h"

@import GoogleMobileAds;

@interface OCRViewController : UIViewController{
    
    UIView* _headerView;
    UITextView* _resultView;
    UIButton* _shareButton;
    
    NSLayoutConstraint* _resultBtm;
    NSLayoutConstraint* _bannerHeight;
}
@property(nonatomic, strong) GADBannerView* bannerView;
@property(nonatomic, strong) UIImage* rawImage;

@end
