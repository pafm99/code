

#import <UIKit/UIKit.h>
#import <Social/Social.h>

@import GoogleMobileAds;


@interface ShareViewController : UIViewController<UITableViewDataSource, UITableViewDelegate,GADInterstitialDelegate>{
    
    UIView* _headerView;
    UITableView* _shareListView;
    UIImageView* _thumbnailImageView;
    
    NSArray* _contentArray;
    
    NSLayoutConstraint* _bannerHeight;
}
@property(nonatomic, strong) UIImage* savedImage;
@property(nonatomic,strong) GADInterstitial* interstitial;
@property(nonatomic, strong) GADBannerView* bannerView;
@end
