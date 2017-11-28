

#import <Foundation/Foundation.h>

#define kAdmobAdsenseFullScreenUnitID @"ca-app-pub-4348791692890867/4436207424"
#define kAdmobAdsenseBannerUnitID @"ca-app-pub-4348791692890867/5912940629"

@import GoogleMobileAds;

@interface DefaultValues : NSObject

+(NSString *)languageToRecognize;
+(NSArray *)adsenseTestDevices;
+(BOOL)isAdmobActive;


@end
