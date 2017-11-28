

#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>

#import <TesseractOCR/TesseractOCR.h>

@interface ImageRecognizer : NSObject

+(ImageRecognizer *)sharedRecognizer;

-(void)recognizeImage:(UIImage *)image completion:(void (^) (NSString* result))completion;
                                                          
@end
