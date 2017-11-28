

#import "DefaultValues.h"


@implementation DefaultValues

+(NSString *)languageToRecognize{
    
    return @"eng+rus+kor";
//    return @"jpn+kor+ita+eng+por+rus+chi";
//    return @"chi_sim+jpn+kor+ita+eng+por+rus";
}

+(NSArray *)adsenseTestDevices{
    
    return @[kGADSimulatorID];
}
+(BOOL)isAdmobActive{
    
    return YES;
}
@end
