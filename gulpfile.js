'use strict';

var gulp = require('gulp');
var browserSync = require('browser-sync').create();
var runsequence = require('run-sequence');
var reload = browserSync.reload;

var directory = './medical_prescription/**'
var dist = "./dist"

gulp.task('browserSync', function() {
  browserSync.init({
    open: false,
    notify: false,
    proxy: 'localhost:8000'
  })
});

gulp.task('watch', function() {
  gulp.watch(directory,['files']);
});

gulp.task('reload', function() {
  gulp.watch(dist+"/**").on('change', browserSync.reload);
});

gulp.task('files', function() {
  return gulp.src(directory)
    .pipe(gulp.dest(dist));
});

gulp.task('build', function(cb) {
  runsequence('files', cb);
});

gulp.task('default',['browserSync', 'watch','reload']);
